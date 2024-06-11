import React from 'react';

import './buttons.css';

export function LinkButtonPrimary(props) {
    return (
        <a href={ props.href } className="button btn-primary">
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
