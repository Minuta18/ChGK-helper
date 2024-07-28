import * as React from "react";

import "./pageLayout.css";

interface PageLayoutProps {
    header?: React.ReactNode;
    aside?: React.ReactNode;
    mainContent?: React.ReactNode;
    footer?: React.ReactNode;
    form?: React.ReactNode;
}

export function PageLayout(props: PageLayoutProps) {
    return (
        <div className="page">
            <header className="page__header">
                { props.header }
            </header>
            <div className="page__content">
                { props.aside !== undefined ?
                    <aside className="page__aside">
                        { props.aside }
                    </aside> : <div></div>
                }
                { props.mainContent !== undefined ?
                    <div className="page__mainContent">
                        { props.mainContent }
                    </div> : <div></div>
                }
                { props.form !== undefined ?
                    <div className="page__form">
                        { props.form }
                    </div> : <div></div>
                }
            </div>
            <footer>
                { props.footer }
            </footer>
        </div>
    );
}
