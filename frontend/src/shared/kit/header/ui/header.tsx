import React from "react";

interface HeaderProps {
    underlined?: boolean;
    children?: React.ReactNode[] | React.ReactNode;
}

export function Header({ underlined = true, children }: HeaderProps) {
    return (
        <div className={ 
            underlined ? "heading-text underlined-text" :
            "heading-text" 
        }>
            { children}
        </div>
    );
}
