import React from 'react';

import '../../assets/background.svg'
import './modal.css';

export default function Modal(props) {
    return (
        <div className="modal">
            { props.children }
        </div>
    );
}