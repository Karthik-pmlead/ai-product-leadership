import streamlit as st
import pandas as pd
import psycopg2
import uuid
from datetime import datetime

# Function to connect to Redshift
def get_redshift_connection():
    conn = psycopg2.connect(
        dbname='dev',
        host='redshift-cluster-1.cyhjrljxgyvk.ap-south-1.redshift.amazonaws.com',
        port='5439',  # default Redshift port
        user='awsuser',
        password='Redshift123'
    )
    return conn

# Function to execute queries
def execute_query(query, params=None):
    conn = get_redshift_connection()
    cur = conn.cursor()
    try:
        print(f"Executing query: {query} with params: {params}")
        cur.execute(query, params)
        conn.commit()
        print("Query executed successfully")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        conn.close()

# Fetch products from Redshift (products table)
def fetch_products():
    query = "SELECT * FROM products;"
    conn = get_redshift_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Fetch customer info from Redshift (customers table)
def fetch_customer_info(customer_unique_id):
    query = "SELECT * FROM customers WHERE customer_unique_id = %s;"
    conn = get_redshift_connection()
    df = pd.read_sql(query, conn, params=(customer_unique_id,))
    conn.close()
    return df

# Function to check user login
def login_user(username, password):
    # Simple login simulation (use DB or external service in production)
    # Here, we map the username to the customer_unique_id
    customer_mapping = {
        'testuser': '861eff4711a542e4b93843c6dd7febb0'  # You can add more mappings as needed
    }

    if username in customer_mapping and password == "testpassword":
        return customer_mapping[username]
    return None

# Add to cart functionality (stored in session state)
def add_to_cart(product_id, quantity):
    if 'cart' not in st.session_state:
        st.session_state.cart = []
    
    st.session_state.cart.append({'product_id': product_id, 'quantity': quantity})
    st.success(f'Added {quantity} of Product ID {product_id} to your cart.')

# Checkout function
def checkout():
    if 'cart' not in st.session_state or len(st.session_state.cart) == 0:
        st.warning("Your cart is empty!")
        return None

    # Display cart items
    cart_df = pd.DataFrame(st.session_state.cart)
    products = fetch_products()
    
    # Merge cart data with product details, using product_id
    cart_df = cart_df.merge(products[['product_id', 'product_category_name', 'product_name_length']], on='product_id', how='left')
    
    # Calculate total price (here, I use `product_name_length` as a placeholder for price)
    cart_df['total_price'] = cart_df['product_name_length'] * 2  # Example calculation for price (adjust as needed)
    
    st.write(cart_df)
    
    # Calculate total (adjust the formula accordingly)
    total_amount = cart_df['total_price'].sum()
    st.write(f"Total Amount: ${total_amount:.2f}")
    
    return cart_df, total_amount

# Store the order and related data into Redshift
def store_order_and_transaction(customer_unique_id, cart_df, total_amount):
    # Fetch customer details
    customer_info = fetch_customer_info(customer_unique_id)
    if customer_info.empty:
        st.error(f"Customer with ID {customer_unique_id} not found.")
        return None

    customer_id = customer_info['customer_id'].iloc[0]  # Get actual customer_id from DB
    order_id = str(uuid.uuid4())  # Generate unique order ID
    transaction_id = str(uuid.uuid4())  # Generate unique transaction ID
    order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    order_status = 'approved'

    # Insert into orders table
    order_query = """
        INSERT INTO orders (order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at)
        VALUES (%s, %s, %s, %s, %s);
    """
    execute_query(order_query, (order_id, customer_id, order_status, order_date, order_date))

    # Insert into order_items table
    for index, row in cart_df.iterrows():
        order_item_query = """
            INSERT INTO order_items (order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        order_item_id = index + 1  # Assuming order_item_id is an index starting from 1
        seller_id = "default_seller"  # Replace with actual seller info if needed
        shipping_limit_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Placeholder for shipping limit
        price = row['total_price']
        freight_value = 0  # You can calculate or retrieve freight costs based on your business logic
        execute_query(order_item_query, (order_id, order_item_id, row['product_id'], seller_id, shipping_limit_date, price, freight_value))

    # Insert into payments table
    payment_id = str(uuid.uuid4())  # Generate unique payment ID
    payment_query = """
        INSERT INTO payments (order_id, payment_sequential, payment_type, payment_installments, payment_value)
        VALUES (%s, %s, %s, %s, %s);
    """
    execute_query(payment_query, (order_id, 1, 'credit_card', 1, float(total_amount)))

    # Insert into transactions table
    transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction_query = """
        INSERT INTO order_reviews (review_id, order_id, review_score, review_comment_title, review_comment_message, review_creation_date, review_answer_timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    review_id = str(uuid.uuid4())  # Generate unique review ID (this can be left blank for now or added later)
    execute_query(transaction_query, (review_id, order_id, 5, 'Great product!', 'I am happy with my purchase', transaction_date, transaction_date))

    st.success("Transaction completed and stored in Redshift!")

    # Return order_id so it can be displayed in the app
    return order_id

# Function to fetch the most recent order from the database
def get_latest_order():
    query = "SELECT order_id FROM orders ORDER BY order_purchase_timestamp DESC LIMIT 1;"
    conn = get_redshift_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df['order_id'].iloc[0] if not df.empty else None

# Streamlit UI
st.title("Olist Ecommerce - User Login")

# Login section
if 'user_logged_in' not in st.session_state:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    login_button = st.button("Login")
    if login_button:
        customer_unique_id = login_user(username, password)
        if customer_unique_id:
            st.session_state.user_logged_in = True
            st.session_state.user_unique_id = customer_unique_id  # Save customer_unique_id for use later
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")

# If logged in, show product catalog with pagination
if 'user_logged_in' in st.session_state and st.session_state.user_logged_in:
    st.subheader("Product Catalog")
    
    # Fetch all products from Redshift
    products = fetch_products()

    # Set pagination parameters
    items_per_page = 10  # Number of products per page
    total_pages = len(products) // items_per_page + (1 if len(products) % items_per_page > 0 else 0)

    # Initialize session state for page tracking if not already set
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 0

    # Show the current page products
    start_idx = st.session_state.current_page * items_per_page
    end_idx = min(start_idx + items_per_page, len(products))
    products_page = products.iloc[start_idx:end_idx]

    # Display products on current page
    for idx, row in products_page.iterrows():
        st.write(f"Product ID: {row['product_id']} - Category: {row['product_category_name']}")
        quantity = st.number_input(f"Quantity for Product ID {row['product_id']}", min_value=0, max_value=10, key=row['product_id'])
        if st.button(f"Add to Cart {row['product_id']}", key=f"add_{row['product_id']}"):
            add_to_cart(row['product_id'], quantity)

    # Pagination buttons
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        if st.session_state.current_page > 0:
            if st.button("Previous Page"):
                st.session_state.current_page -= 1

    with col2:
        st.write(f"Page {st.session_state.current_page + 1} of {total_pages}")

    with col3:
        if st.session_state.current_page < total_pages - 1:
            if st.button("Next Page"):
                st.session_state.current_page += 1

    # Checkout section
    if len(st.session_state.cart) > 0:
        checkout_button = st.button("Proceed to Checkout")
        if checkout_button:
            cart_df, total_amount = checkout()
            if cart_df is not None:
                order_id = store_order_and_transaction(st.session_state.user_unique_id, cart_df, total_amount)
                if order_id:
                    st.success(f"Order placed successfully! Order ID: {order_id}")
                    latest_order_id = get_latest_order()  # Fetch the latest order ID from DB
                    st.write(f"The latest order ID is: {latest_order_id}")

