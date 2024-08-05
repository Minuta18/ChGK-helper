import { ReactNode } from "react";
import { NavLink } from "react-router-dom";

interface HeaderLinkProps {
    to: string;
    children?: ReactNode;
}

export function HeaderLink(props: HeaderLinkProps) {
    return (
        <NavLink to={props.to}>
            {({isActive, isPending, isTransitioning}) => {
                return <span className={
                    isActive ? "header__element-inner active" : 
                        "header__element-inner not-active"
                }>
                    { props.children }
                </span>;
            }}
        </NavLink>
    );
}
