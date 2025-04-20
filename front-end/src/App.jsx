import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/home";
import AddProduct from "./AddProduct";
import ProductDetail from "./ProductDetail";


export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/add" element={<AddProduct />} />
        <Route path="/product/:id" element={<ProductDetail />} />
      </Routes>
    </Router>
  )
}
