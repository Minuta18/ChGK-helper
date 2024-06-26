import React from 'react';
import { BsArrowLeftShort, BsGear } from 'react-icons/bs';
import { useNavigate } from 'react-router-dom';

import './buttons.css';

export function LinkButtonPrimary(props) {
    let btnClassName = "button btn-primary";
    
    if (props.disabled) {
        btnClassName = "button btn-primary blocked-primary";
    }

    return (
        <a href={ props.href } className={ btnClassName }
            onClick={ props.onClick }
        >
            { props.children }
        </a>
    );
}

export function LinkButtonSecondary(props) {
    return (
        <a href={ props.href } className="button btn-secondary"
            onClick={ props.onClick }
        >
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

export function SettingsButton() {
    let navigate = useNavigate();

    return (
        <BsGear className='settings-button' onClick={() => {
            navigate('/settings');
        }} />
    );
}

export function ButtonPrimary(props) {
    let btnClassName = "button btn-primary";
    
    if (props.disabled) {
        btnClassName = "button btn-primary blocked-primary";
    }

    return (
        <button className={ btnClassName } onClick={ props.onClick }>
            { props.children }
        </button>
    );
}

export function ButtonSecondary(props) {
    let btnClassName = "button btn-secondary";
    
    if (props.disabled) {
        btnClassName = "button btn-secondary blocked-secondary";
    }

    return (
        <button className={ btnClassName } onClick={ props.onClick }>
            { props.children }
        </button>
    );
}

