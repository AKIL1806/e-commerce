import React from 'react'
import { motion } from 'framer-motion'

export default function ProductCard({ name, price, image }) {
  return (
    <motion.div
      className="product-card"
      whileHover={{ scale: 1.05, rotate: 1 }}
      transition={{ type: 'spring', stiffness: 300 }}
    >
      <img src={image} alt={name} style={{ width: '100%', borderRadius: '12px' }} />
      <h3>{name}</h3>
      <p>{price}</p>
      <button>Add to Cart</button>
    </motion.div>
  )
}
