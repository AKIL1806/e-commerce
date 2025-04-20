import React from 'react'
import { useParams } from 'react-router-dom'

export default function ProductDetail() {
  const { id } = useParams()

  return (
    <div className="page">
      <h1>Product Details - {id}</h1>
      <p>More details to come...</p>
    </div>
  )
}
