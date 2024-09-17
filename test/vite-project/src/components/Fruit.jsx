import React from 'react'

function Fruit({name,price}) {
  return (
    <li key={name}> {price>100?<h3>The price of {name} is {price}</h3>:""}</li>
  )
}

export default Fruit