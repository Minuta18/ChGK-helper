import * as React from "react";

import "./container.css";

interface ContainerProps {
    children?: React.ReactNode[]|React.ReactNode;
}

export function Container(props: ContainerProps){
    return (
        <div className="default-container">
            { props.children }
        </div>
    );
}
