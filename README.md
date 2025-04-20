# 🧪 Test Scenarios, Test Cases, and Bug Reports

We have documented our testing efforts, including detailed test scenarios, test cases, and identified bugs. You can access the full spreadsheet using the link below:

**[👉 Test Scenarios and Reports](https://docs.google.com/spreadsheets/d/1TimR_jwK6ORmGtT8tisawo_rVS_w6_CKpQCX_FQMHQc/edit?usp=sharing)**:
https://docs.google.com/spreadsheets/d/1TimR_jwK6ORmGtT8tisawo_rVS_w6_CKpQCX_FQMHQc/edit?usp=sharing
Feel free to explore for detailed insights!


  <h1>📘 Bookstore Web App</h1>

  <div class="section">
    <h2>📦 Required to operate</h2>
    <ul>
      <li><strong>Python</strong></li>
      <li>Flask API</li>
      <li>SQLAlchemy (ORM)</li>
    </ul>
  </div>

  <div class="section">
    <h2>📝 Project Description</h2>
    <p>This web application create for pratices testing purpose</p>
  </div>

  <div class="section">
    <h2>🔧 Main Features / Components</h2>
    <ul>
      <li><strong>Authentication</strong>
        <ul>
          <li>Login with Username / Phone Number / Email</li>
          <li>Registration form with validation:
            <ul>
              <li>Name (no numbers or special characters)</li>
              <li>Birthdate</li>
              <li>Email (correct format)</li>
              <li>Phone Number (9 digits)</li>
              <li>Username</li>
              <li>Gender (radio buttons)</li>
              <li>Nation (dropdown)</li>
              <li>Password / Confirm Password (show/hide, block copy-paste)</li>
              <li>Terms & Conditions (checkbox)</li>
            </ul>
          </li>
          <li>Forgot Password via Email</li>
        </ul>
      </li>
      <li><strong>Book Management (CRUD)</strong>
        <ul>
          <li>Fields: Title, Description, Category, Author, Quantity (in store), Full Pay Price, Rent Price, Published Year</li>
          <li>Image upload for book cover (drag & drop or file select)</li>
          <li>File upload for book content (only specific file types)</li>
        </ul>
      </li>
      <li><strong>Category Management (CRUD)</strong>
        <ul>
          <li>Sort A->Z and Z -> A </li>
        </ul>
      </li>
      <li><strong>Cart System</strong>
        <ul>
          <li>Add to Cart</li>
          <li>Checkout</li>
          <li>Download purchased book files</li>
        </ul>
      </li>
      <li><strong>User Roles</strong>
        <ul>
          <li>Assign role for readers (normal user, writer, admin)</li>
        </ul>
      </li>
      <li><strong>Comment System</strong> (on each book detail page)</li>
      <li><strong>UI/UX Enhancements</strong>
        <ul>
          <li>Hover effects</li>
          <li>Disabled buttons when needed</li>
          <li>JavaScript notifications</li>
          <li>Modal components</li>
          <li>Sortable tables</li>
          <li>Infinite scrolling / "Load More" feature</li>
        </ul>
      </li>
      <li><strong>Layout</strong>
        <ul>
          <li>Header</li>
          <li>Footer</li>
          <li>Side Navigation With Jquery UI menu</li>
        </ul>
      </li>
    </ul>
  </div>
  <br>
  <h1>API Specification</h1>
<p>note: the application only contains post and get due to litmited of HTML Form</p>
<p><strong>Base URL:</strong> http://localhost:5000</p>

<h2>🛡️ Auth </h1>
<p><strong>Base URL:</strong> http://localhost:5000</p>

<li><strong>Auth</strong></li>
<ul>
  <li><strong>GET</strong> /register</li>
  <ul>
    <li>Description: Render the registration form</li>
    <li>Response: render <code>auth/register.html</code></li>
  </ul>

  <li><strong>POST</strong> /register</li>
  <ul>
    <li>Description: Register a new reader</li>
    <li>Request Body (form): full_name, birthdate, gmail, gender, nation, phone, username, password, confirm_password</li>
    <li>Response: Redirect to <code>/login</code> or flash error</li>
  </ul>

  <li><strong>GET</strong> /login</li>
  <ul>
    <li>Description: Render the login form</li>
    <li>Response: render <code>auth/login.html</code></li>
  </ul>

  <li><strong>POST</strong> /login</li>
  <ul>
    <li>Description: Authenticate reader by username, email, or phone</li>
    <li>Request Body (form): identifier, password</li>
    <li>Response: Render home page or flash error</li>
  </ul>

  <li><strong>GET</strong> /forgot-password</li>
  <ul>
    <li>Description: Render the forgot password form</li>
    <li>Response: render <code>auth/forgot_password.html</code></li>
  </ul>

  <li><strong>POST</strong> /forgot-password</li>
  <ul>
    <li>Description: Simulate sending password reset instructions</li>
    <li>Request Body (form): username_or_email</li>
    <li>Response: Flash success or error, redirect to <code>/login</code></li>
  </ul>

  <li><strong>GET</strong> /logout</li>
<ul>
  <li>Description: Logs out the current reader</li>
  <li>Response: Flash success message, redirect to <code>/login</code></li>
</ul>
</ul>




<h2>📁 Category</h2>
<p><strong>Base URL:</strong> http://localhost:5000</p>
<ul>
  <li><strong>GET</strong> /categories</li>
  <ul>
    <li><strong>Description:</strong> Retrieves list of categories</li>
    <li><strong>Response:</strong> Renders <code>list.html</code></li>
  </ul>

  <li><strong>GET</strong> /categories/create</li>
  <ul>
    <li><strong>Description:</strong> Display form to create a new category</li>
    <li><strong>Response:</strong> Renders <code>create.html</code></li>
  </ul>

  <li><strong>POST</strong> /categories/create</li>
  <ul>
    <li><strong>Description:</strong> Submit form to create a category</li>
    <li><strong>Request Body:</strong> <code>name</code> (form-data)</li>
    <li><strong>Response:</strong> Redirects to <code>/categories</code></li>
  </ul>

  <li><strong>GET</strong> /categories/edit/&lt;id&gt;</li>
  <ul>
    <li><strong>Description:</strong> Show form to edit category by ID</li>
    <li><strong>Response:</strong> Renders <code>edit.html</code> with category data</li>
  </ul>

  <li><strong>POST</strong> /categories/edit/&lt;id&gt;</li>
  <ul>
    <li><strong>Description:</strong> Submit updated category data</li>
    <li><strong>Request Body:</strong> <code>name</code> (form-data)</li>
    <li><strong>Response:</strong> Redirects to <code>/categories</code></li>
  </ul>

  <li><strong>GET</strong> /categories/delete/&lt;id&gt;</li>
  <ul>
    <li><strong>Description:</strong> Delete category by ID</li>
    <li><strong>Response:</strong> Redirects to <code>/categories</code></li>
  </ul>
</ul>

<h2>📕 Book</h2>
<p><strong>Base URL:</strong> http://localhost:5000</p>
<ul>
  <li><strong>GET</strong> /books</li>
  <ul>
    <li>Description: List all books</li>
    <li>Response: Renders <code>book/book_list.html</code> with all books</li>
  </ul>

  <li><strong>GET</strong> /books/create</li>
  <ul>
    <li>Description: Show book creation form</li>
    <li>Response: Renders <code>book/book_create.html</code></li>
  </ul>

  <li><strong>POST</strong> /books/create</li>
  <ul>
    <li>Description: Create a new book</li>
    <li>Request: Form data with title, description, category_id, author_id, published, quantity, fullpay_price, rent_price, cover_image, book_file</li>
    <li>Response: Redirect to <code>/books</code></li>
  </ul>

  <li><strong>GET</strong> /books/edit/&lt;book_id&gt;</li>
  <ul>
    <li>Description: Show edit form for a book</li>
    <li>Response: Renders <code>book/book_edit.html</code></li>
  </ul>

  <li><strong>POST</strong> /books/edit/&lt;book_id&gt;</li>
  <ul>
    <li>Description: Update book information</li>
    <li>Request: Form data similar to creation</li>
    <li>Response: Redirect to <code>/books</code></li>
  </ul>

  <li><strong>GET</strong> /books/delete/&lt;book_id&gt;</li>
  <ul>
    <li>Description: Delete a book and related comments/cart items</li>
    <li>Response: Redirect to <code>/books</code></li>
  </ul>

  <li><strong>GET, POST</strong> /books/&lt;book_id&gt;</li>
  <ul>
    <li>Description: View book details and comments, or add a new comment</li>
    <li>POST Request: content, reader_id</li>
    <li>Response: Renders <code>book/book_detail.html</code></li>
  </ul>

  <li><strong>POST</strong> /comments/delete/&lt;comment_id&gt;</li>
  <ul>
    <li>Description: Delete a comment</li>
    <li>Response: Redirect to book detail page</li>
  </ul>

  <li><strong>GET</strong> /</li>
  <ul>
    <li>Description: Homepage with limited list of books</li>
    <li>Response: Renders <code>Homepage/home.html</code></li>
  </ul>

  <li><strong>GET</strong> /books/load?offset=&lt;int&gt;&limit=&lt;int&gt;</li>
  <ul>
    <li>Description: Load more books for pagination</li>
    <li>Response: JSON with book details</li>
  </ul>
</ul>

<h2>👤 Reader</h2>
<p><strong>Base URL:</strong> http://localhost:5000</p>
<ul>
  <li><strong>GET</strong> /readers</li>
  <ul>
    <li>Description: Paginated list of all readers</li>
    <li>Query Params: <code>page</code> (optional, default = 1)</li>
    <li>Response: Renders <code>reader/reader_list.html</code> with readers and pagination</li>
  </ul>

  <li><strong>GET</strong> /readers/edit/&lt;reader_id&gt;</li>
  <ul>
    <li>Description: Show form to update a reader's role</li>
    <li>Response: Renders <code>reader/reader_edit.html</code> with reader info and a random key</li>
  </ul>

  <li><strong>POST</strong> /readers/edit/&lt;reader_id&gt;</li>
  <ul>
    <li>Description: Update the reader's role</li>
    <li>Request: Form data with <code>role</code></li>
    <li>Response: Redirects to <code>/readers</code></li>
  </ul>

  <li><strong>GET</strong> /readers/delete/&lt;reader_id&gt;</li>
  <ul>
    <li>Description: Delete a reader by ID</li>
    <li>Response: Redirects to <code>/readers</code></li>
  </ul>

  <li><strong>GET</strong> /readers/block/&lt;reader_id&gt;</li>
  <ul>
    <li>Description: Toggle block/unblock status of a reader</li>
    <li>Logic: Sets role to 4 (blocked) if currently not, otherwise resets to 1 (normal user)</li>
    <li>Response: Redirects to <code>/readers</code> with a flash message</li>
  </ul>
</ul>
<h2>🛒 Cart</h2>
<p><strong>Base URL:</strong> http://localhost:5000</p>
<ul>
  <li><strong>POST</strong> /api/cart/add</li>
  <ul>
    <li>Description: Add a book to the current reader's cart</li>
    <li>Request (JSON): <code>book_id</code>, <code>quantity</code> (default 1)</li>
    <li>Response (JSON): <code>success</code>, <code>cartCount</code></li>
  </ul>

  <li><strong>GET</strong> /cart</li>
  <ul>
    <li>Description: View all books in the current reader's cart</li>
    <li>Response: Renders <code>cart/cart.html</code> with cart items</li>
  </ul>

  <li><strong>POST</strong> /remove_from_cart/&lt;cart_id&gt;</li>
  <ul>
    <li>Description: Remove a book from the cart</li>
    <li>Response: Redirects to <code>/cart</code></li>
  </ul>

  <li><strong>POST</strong> /checkout</li>
  <ul>
    <li>Description: Checkout selected books in the cart</li>
    <li>Request: Form data with <code>selected_cart_items</code> (list of cart item IDs)</li>
    <li>Response: Renders <code>cart/checkout.html</code> with selected cart items</li>
  </ul>
</ul>

