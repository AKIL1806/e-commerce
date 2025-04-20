// src/ProductDetail.jsx
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import "./ProductDetail.css";

const ProductDetail = () => {
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8000/products/${id}`)
      .then((res) => res.json())
      .then((data) => setProduct(data))
      .catch((err) => console.error(err));
  }, [id]);

  if (!product) {
    return <p className="loading-msg">Loading product details...</p>;
  }

  return (
    <div className="detail-container">
      <div className="detail-card">
        <img src={product.image_url} alt={product.name} className="detail-image" />
        <h2>{product.name}</h2>
        <p className="detail-desc">{product.description}</p>
        <p className="detail-price">${product.price}</p>
        <button className="buy-button">Add to Cart</button>
      </div>
    </div>
  );
};

export default ProductDetail;
