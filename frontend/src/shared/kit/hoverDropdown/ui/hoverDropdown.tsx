import * as React from "react";

import "./hoverDropdown.css";

import * as useWindowDimensions from "../../../hooks/useWindowDimensions";

interface HoverDropdownProps {
    mainElement: React.ReactNode,
    children: React.ReactNode[],
}

export function HoverDropdown(props: HoverDropdownProps) {
    const [isOpen, setIsOpen] = React.useState<boolean>(false);
    // eslint-disable-next-line
    const [windowWidth, windowHeight] =  
        useWindowDimensions.useWindowDimensions();

    return (<>
        <div className="dropdown" onClick={() => {
            if (windowWidth <= 600) {
                setIsOpen(!isOpen);
            }
        }}>
            { props.mainElement }
            <div className={isOpen ? 
                "dropdown__content dropdown__open" : "dropdown__content"
            }>
                <div className="dropdown__list">
                    { props.children.map((child, ind) => {
                        return <div className="dropdown__item" key={ ind }>
                            { child }
                        </div>
                    }) }
                </div>
            </div>
        </div>
    </>);
}
