import React from 'react'
import './toast.css'

function toast() {
  return (
    <div class="toast active">
        <div class="toast-content">
            <i class="fas fa-solid fa-check check"></i>

            <div class="message">
                <span class="text text-1">Success</span>
                <span class="text text-2">Your mail has been sent</span>
            </div>
        </div>
        <i class="fa-solid fa-xmark close"></i>

        <div class="progress active"></div>
    </div>
  )
}

export default toast