import * as React from "react";

import "./button.css";

interface ButtonProps {
    children?: React.ReactNode | React.ReactNode[];
    disabled?: boolean;
    onClickCallback?: () => void;
}

export function Button(props: ButtonProps) {
    return (
        <button 
            onClick={ props.onClickCallback } className="default-button"
            disabled={ props.disabled }
        >
            { props.children }
        </button>
    );
}
