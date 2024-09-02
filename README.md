# Transportation Automation Project

## Overview

This is a Python-based automation project designed for transporters. The application allows users to manage companies or individual customers they transport goods for. It includes basic features such as viewing invoices, delivery notes, load photos and transportation charges. Users can also add new records, sort them by date, and keep track of each customer's total debt. This project is under development and continues to evolve according to the many problems and needs of drivers. Innovations that will take your transportation experience to a whole new level are coming soon!
## Features

- **User Authentication:**
  - Secure login and registration system.
  - Only authenticated users can access the application.

- **Client Management:**
  - View and manage a list of companies or individual clients.
  - Add, update, or delete client information.

- **Transaction Management:**
  - Track and manage invoices, delivery notes, load photos, and transport charges.
  - Sort records by date for easy tracking.

- **Photo Management:**
  - Upload and view photos associated with each transaction.
  - Store photos securely in the database.

- **Debt Tracking:**
  - Automatically calculate and display the total debt of each client.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/transportation-automation.git
   cd transportation-automation
   
2. **Create a virtual environment:**
   ```bash
   python -m venv env  
   source env/bin/activate  # On Windows: `env\Scripts\activate`

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Set up the database:**
- This project uses Google Cloud SQL.  
  Make sure to configure your connection settings in `config.py`.

- Create the necessary tables by running the provided SQL scripts in the `sql/` directory.


5. **Run the application:**
   ```bash
   python app.py   
## Technologies Used

- **Python**
- **CustomTkinter** for the GUI
- **Google Cloud SQL** for database management
- **CRUD Operations** in `client_model.py`, `photo_model.py`, `transaction_model.py`, and `user_model.py`

## License

This project is licensed under the [Yiğit Ali Sunal Software License Agreement](LICENSE.md).

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.  
For major changes, please open an issue first to discuss what you would like to change.

## Contact

For any questions or inquiries, please contact [Yiğit Ali Sunal](mailto:your.email@example.com).
