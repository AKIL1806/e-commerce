import React from 'react'

export default function AddProduct() {
  return (
    <div className="page">
      <h1>Add Product</h1>
      <form className="form">
        <input type="text" placeholder="Product Name" />
        <input type="text" placeholder="Category" />
        <input type="number" placeholder="Price" />
        <textarea placeholder="Description" />
        <button type="submit">Add</button>
      </form>
    </div>
  )
}
