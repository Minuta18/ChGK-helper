import * as React from "react";

import "./iconButton.css";

interface IconButtonProps {
    children?: React.ReactNode | React.ReactNode[];
    disabled?: boolean;
    onClickCallback?: () => void;
    color?: string;
}

export function IconButton(props: IconButtonProps) {
    return (
        <button 
            className="icon-button" style={{ 
                backgroundColor: props.color,
            }} 
            onClick={ props.onClickCallback }
            disabled={ props.disabled }
        >
            { props.children }
        </button>
    );
}
