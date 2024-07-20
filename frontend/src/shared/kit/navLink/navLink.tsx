import React from "react";

interface NavLinkProps {
    href: string;
    children: React.ReactNode | React.ReactNode[];
}

export function NavLink({ href, children }: NavLinkProps) {
    return (
        <a href={ href }>
            { children }
        </a>
    );
}
