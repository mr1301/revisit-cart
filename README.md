# revisit-cart
This application generates a receipt for a shopping cart.
The application has a user enter the ID of the products they bought, the way a scanner would, and compiles, calculates the total, taxation and (assuming residence in DC), and prints a receipt of the shopping cart.

Configuration
To used this app you will need
1. ID of items bought e,g from barcode
2. Product attributes and values e.g price

Installing
1.To install simply download the link to the app code on the author's github https://github.com/mr1301/revisit-advisor
2.Load the code onto a terminal
3. paste your product list under products
3. Ensure to name keys and atrributes accordingly
run the program, a receipt should be printed.

Packages Used/Needed
This is a very simpistic app you simply need
1. A datetime module to print time on the receipt
2. If you will be reading the csv contents from a file without pasting you need a CSV module.
3. A pytest package for automated tests

Manifest
1.cart.py - this file contains the application
2.cart_test.py - this file contains the automatic tests
3.License file - copyright details
4.ReadMe file - program description & manual

Copyright
This program is licensed under the MIT license, see lincese file for reference

Trouble shooting & known bugs
All essential components for functionality where automatically tested. automatic date testing was limited because the timestamp uses current date & time, meaning asserting would be difficult. Date tests where performed manually.

Author
Mercy Radithupa

Credits
This assignment could not have been completed without the help and guidance of Prof. Rossetti's lectures, videos and examples. In particular for the pytesting this source was helpful: https://github.com/s2t2/shopping-cart-screencast/pull/2/files