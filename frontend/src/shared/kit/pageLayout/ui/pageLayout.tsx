import * as React from "react";

import "./pageLayout.css";

interface PageLayoutProps {
    header?: React.ReactNode;
    aside?: React.ReactNode;
    mainContent?: React.ReactNode;
    footer?: React.ReactNode;
}

export function PageLayout(props: PageLayoutProps) {
    return (
        <div className="page">
            <header className="page__header">
                { props.header }
            </header>
            <div className="page__content">
                <aside className="page__aside">
                    { props.aside }
                </aside>
                <div className="page__mainContent">
                    { props.mainContent }
                </div>
            </div>
            <footer>
                { props.footer }
            </footer>
        </div>
    );
}
