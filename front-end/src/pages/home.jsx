import React from 'react'
import { motion } from 'framer-motion'
import ProductCard from '../components/ProductCard'

const fadeUp = {
  hidden: { opacity: 0, y: 40 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.8 } },
}

export default function Home() {
  return (
    <div className="page">
      {/* Navbar */}
      <nav className="navbar">
        <h2 className="logo">Aura</h2>
        <div className="nav-links">
          <a href="#">Home</a>
          <a href="#">Login</a>
          <a href="#">Signup</a>
        </div>
      </nav>

      {/* Hero Section */}
      <motion.section
        className="hero"
        variants={fadeUp}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
      >
        <div className="hero-content">
          <h1>Welcome to Aura</h1>
          <p>Where future meets fashion & tech.</p>
          <button>Start Shopping</button>
        </div>
      </motion.section>

      {/* Categories */}
      <motion.section
        className="categories"
        variants={fadeUp}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
      >
        <h2>Categories</h2>
        <div className="category-grid">
          <div className="category-card">Clothing</div>
          <div className="category-card">Mobiles</div>
          <div className="category-card">Laptops</div>
          <div className="category-card">Kitchen</div>
          <div className="category-card">Books</div>
        </div>
      </motion.section>

      {/* Featured Products */}
      <motion.section
        className="featured-products"
        variants={fadeUp}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
      >
        <h2>Featured Products</h2>
        <div className="product-grid">
          <ProductCard name="PulseBand" price="$199" image="/pulse-band.jpg" />
          <ProductCard name="HoverSneaks" price="$299" image="/hover-sneaks.jpg"/>
          <ProductCard name="VoidCam" price="$649" image="/void-cam.png" />
          <ProductCard name="SmartMirror X" price="$199" image="/smart-mirror.jpg"/>
        </div>
      </motion.section>

      {/* Newsletter Signup */}
      <motion.section
        className="newsletter"
        variants={fadeUp}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
      >
        <h2>Stay in the Loop</h2>
        <p>Sign up for exclusive offers and futuristic product drops.</p>
        <div className="newsletter-form">
          <input type="email" placeholder="Your email" />
          <button>Subscribe</button>
        </div>
      </motion.section>

      {/* Footer */}
      <footer className="footer">
        <p>&copy; 2025 Aura. All rights reserved.</p>
        <div className="socials">
          <a href="#">Instagram</a>
          <a href="#">Twitter</a>
          <a href="#">Facebook</a>
        </div>
      </footer>
    </div>
  )
}
