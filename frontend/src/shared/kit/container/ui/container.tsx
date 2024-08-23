import * as React from "react";

import "./container.css";

interface ContainerProps {
    children?: React.ReactNode[]|React.ReactNode;
    style?: Object;
}

export function Container(props: ContainerProps){
    return (
        <div className="default-container" style={ props.style }>
            { props.children }
        </div>
    );
}
