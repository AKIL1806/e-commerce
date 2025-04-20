import { useEffect, useState } from 'react';

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/products/')
      .then(res => res.json())
      .then(data => setProducts(data))
      .catch(err => console.error("Error fetching products:", err));
  }, []);

  return (
    <div style={{ padding: '2rem', color: 'white', background: 'black', minHeight: '100vh' }}>
      <h1 style={{ fontSize: '2rem', marginBottom: '2rem' }}>Available Products</h1>

      {products.length === 0 ? (
        <p>No products available.</p>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '1rem' }}>
          {products.map((product, i) => (
            <div key={i} style={{ border: '1px solid #444', borderRadius: '8px', padding: '1rem' }}>
              <h2>{product.name}</h2>
              <p>Price: ${product.price}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
