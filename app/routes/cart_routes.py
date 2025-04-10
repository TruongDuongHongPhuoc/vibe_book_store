from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from app.models.cart_model import Cart
from app import db
from app.models.book_model import Book  # Import the Book model
from app.models.currentReader import currentReader
cart_routes = Blueprint('cart_routes', __name__)

# NOTE: the following code assumes that the user is alway have id 1 and only 1 user in the system.
# Add book to cart

@cart_routes.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()

    # Extract the book ID and quantity from the request
    book_id = data.get('book_id')
    quantity = data.get('quantity', 1)

    if not book_id or quantity <= 0:
        return jsonify({'success': False, 'message': 'Invalid data'}), 400

    
    book = Book.query.get(book_id)  # Fetch the book directly using the Book model
    if not book:
        return jsonify({'success': False, 'message': 'Book not found'}), 404

    # Check if the book is already in the user's cart
    existing_cart_item = Cart.query.filter_by(book_id=book_id, reader_id=currentReader.id).first()

    if existing_cart_item:
        existing_cart_item.quantity += quantity
        existing_cart_item.total_price = existing_cart_item.price_per_unit * existing_cart_item.quantity
    else:
        cart_item = Cart(
            quantity=quantity,
            price_per_unit=book.full_pay_price,
            rent_or_purchase='purchase',  # Assuming purchase for simplicity
            book_id=book.id,
            reader_id= currentReader.id
        )
        db.session.add(cart_item)

    db.session.commit()

    # Return the new cart item count
    cart_count = Cart.query.filter_by(reader_id=currentReader.id).count()
    return jsonify({'success': True, 'cartCount': cart_count})

# View cart
@cart_routes.route('/cart')
def view_cart():
    user_cart = Cart.query.filter_by(reader_id=currentReader.id).all()
    return render_template('cart/cart.html', cart_items=user_cart)

# Remove book from cart
@cart_routes.route('/remove_from_cart/<int:cart_id>', methods=['POST'])
def remove_from_cart(cart_id):
    cart_item = Cart.query.get(cart_id)
    db.session.delete(cart_item)
    db.session.commit()
    return redirect(url_for('cart_routes.view_cart'))

@cart_routes.route('/checkout', methods=['POST'])
def checkout():
    reader_id = currentReader.id  # Replace with session-based user ID in the future
    selected_ids = request.form.getlist('selected_cart_items')

    if not selected_ids:
        flash('No items selected for checkout.')
        return redirect(url_for('cart_routes.view_cart'))

    cart_items = Cart.query.filter(Cart.id.in_(selected_ids), Cart.reader_id == reader_id).all()
    return render_template('cart/checkout.html', cart_items=cart_items)


