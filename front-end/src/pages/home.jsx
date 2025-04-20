import React from 'react'
import ProductCard from '../components/ProductCard'

export default function Home() {
  return (
    <div className="page">
      <h1>Shop The Future</h1>

      <div className="product-grid">
        <ProductCard
          name="HoloPhone Z"
          price="$999"
          image="https://via.placeholder.com/300x200?text=HoloPhone+Z"
        />
        <ProductCard
          name="Quantum Lamp"
          price="$249"
          image="https://via.placeholder.com/300x200?text=Quantum+Lamp"
        />
        <ProductCard
          name="AI SmartBook"
          price="$499"
          image="https://via.placeholder.com/300x200?text=AI+SmartBook"
        />
        <ProductCard
          name="Neon Sneakers"
          price="$199"
          image="https://via.placeholder.com/300x200?text=Neon+Sneakers"
        />
      </div>
    </div>
  )
}
