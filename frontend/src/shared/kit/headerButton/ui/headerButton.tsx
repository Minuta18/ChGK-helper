import * as React from "react";

import "./headerButton.css";

interface HeaderButtonProps {
    children?: React.ReactNode | React.ReactNode[];
    disabled?: boolean;
    onClickCallback?: () => void;
}

export function HeaderButton(props: HeaderButtonProps) {
    return (
        <button 
            onClick={ props.onClickCallback } className="header-button"
            disabled={ props.disabled }
        >
            { props.children }
        </button>
    );
}
