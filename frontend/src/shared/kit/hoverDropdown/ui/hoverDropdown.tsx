import { ReactNode } from "react";

import "./hoverDropdown.css";

interface HoverDropdownProps {
    mainElement: ReactNode,
    children: ReactNode[],
}

export function HoverDropdown(props: HoverDropdownProps) {
    return (<>
        <div className="dropdown">
            { props.mainElement }
            <div className="dropdown__content">
                <div className="dropdown__list">
                    { props.children.map((child) => {
                        return <div className="dropdown__item" key={ 
                            crypto.randomUUID() 
                        }>
                            { child }
                        </div>
                    }) }
                </div>
            </div>
        </div>
    </>);
}
