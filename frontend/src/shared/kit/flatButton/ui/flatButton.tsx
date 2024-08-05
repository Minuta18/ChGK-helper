import * as React from "react";

import "./flatButton.css";

interface FlatButtonProps {
    children?: React.ReactNode | React.ReactNode[];
    disabled?: boolean;
    onClickCallback?: () => void;
}

export function FlatButton(props: FlatButtonProps) {
    return (
        <button 
            onClick={ props.onClickCallback } className="flat-button"
            disabled={ props.disabled }
        >
            { props.children }
        </button>
    );
}
