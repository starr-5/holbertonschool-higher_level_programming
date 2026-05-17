from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv_file():
    products = []

    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })

    return products


def read_sql_file():
    products = []

    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()

        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })

        conn.close()

    except sqlite3.Error:
        return None

    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validate source
    if source not in ['json', 'csv', 'sql']:
        return render_template(
            'product_display.html',
            error='Wrong source'
        )

    # Read data based on source
    if source == 'json':
        products_data = read_json_file()

    elif source == 'csv':
        products_data = read_csv_file()

    else:
        products_data = read_sql_file()

        if products_data is None:
            return render_template(
                'product_display.html',
                error='Database error'
            )

    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)

            filtered_products = [
                product for product in products_data
                if product['id'] == product_id
            ]

            if not filtered_products:
                return render_template(
                    'product_display.html',
                    error='Product not found'
                )

            products_data = filtered_products

        except ValueError:
            return render_template(
                'product_display.html',
                error='Product not found'
            )

    return render_template(
        'product_display.html',
        products=products_data
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)