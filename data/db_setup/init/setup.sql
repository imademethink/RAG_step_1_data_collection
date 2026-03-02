-- 1. Create Tables
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES categories(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    sku VARCHAR(50) UNIQUE NOT NULL,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Seed Initial Categories
INSERT INTO categories (name, slug) VALUES 
('Electronics', 'electronics'), 
('Clothing', 'clothing'), 
('Home & Garden', 'home-garden'),
('Sports', 'sports');

-- 3. Seed 200 Sample Products using a Loop
DO $$
BEGIN
    FOR i IN 1..200 LOOP
        INSERT INTO products (category_id, name, description, price, sku, image_url)
        VALUES (
            (SELECT id FROM categories ORDER BY RANDOM() LIMIT 1),
            'Product Item ' || i,
            'This is a high-quality description for product number ' || i || '.',
            (RANDOM() * 500 + 10)::NUMERIC(10,2),
            'SKU-' || LPAD(i::text, 5, '0'),
            'https://via.placeholder.com+' || i
        );
    END LOOP;
END $$;

-- ==========================================
-- TABLE: categories
-- ==========================================
COMMENT ON TABLE categories IS 'Stores the product classification hierarchy for navigation and filtering.';
COMMENT ON COLUMN categories.id IS 'Primary key: Unique identifier for the category.';
COMMENT ON COLUMN categories.name IS 'Display name of the category (e.g., "Electronics").';
COMMENT ON COLUMN categories.slug IS 'URL-friendly version of the name, used for SEO-friendly routing.';

-- ==========================================
-- TABLE: products
-- ==========================================
COMMENT ON TABLE products IS 'Main catalog table containing all items available for purchase.';
COMMENT ON COLUMN products.id IS 'Primary key: Unique identifier for the product.';
COMMENT ON COLUMN products.category_id IS 'Foreign key: Links the product to its parent category.';
COMMENT ON COLUMN products.name IS 'Full title of the product as shown to the customer.';
COMMENT ON COLUMN products.description IS 'Detailed marketing text or technical specifications of the product.';
COMMENT ON COLUMN products.price IS 'Current selling price. Stored as DECIMAL to ensure financial accuracy.';
COMMENT ON COLUMN products.sku IS 'Stock Keeping Unit: A unique merchant-defined code for inventory tracking.';
COMMENT ON COLUMN products.image_url IS 'Path or full URL to the primary product image.';
COMMENT ON COLUMN products.created_at IS 'Audit timestamp for when the product was added to the catalog.';
