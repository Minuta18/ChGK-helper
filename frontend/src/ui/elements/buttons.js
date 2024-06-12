import React from 'react';
import { BsArrowLeftShort } from 'react-icons/bs';
import { useNavigate } from 'react-router-dom';

import './buttons.css';

export function LinkButtonPrimary(props) {
    let btnClassName = "button btn-primary";
    
    if (props.disabled) {
        btnClassName = "button btn-primary blocked-primary";
    }

    return (
        <a href={ props.href } className={ btnClassName }>
            { props.children }
        </a>
    );
}

export function LinkButtonSecondary(props) {
    return (
        <a href={ props.href } className="button btn-secondary">
            { props.children }
        </a>
    );
}

export function BackButton() {
    let navigate = useNavigate();

    return (
        <BsArrowLeftShort className='back-button' onClick={() => {
            navigate(-1);
        }} />
    );
}
