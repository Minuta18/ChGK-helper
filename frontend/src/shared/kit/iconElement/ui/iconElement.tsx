import React from "react";

import "./iconElement.css";

interface IconElementProps {
    icon?: React.ReactNode;
    children: React.ReactNode[] | React.ReactNode;
    className?: string;
}

export function IconElement(props: IconElementProps) {
    return (
        <div className={ props.className } style={{
            display: 'block',
            width: '100%',
        }}>
            <div className="icon-element">
                <div className="icon-element__icon">
                    { props.icon }
                </div>
                { props.children }
            </div>
        </div>
    );
}
