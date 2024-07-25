import * as React from "react";

function getWindowDimensions(): [number, number] {
    const { innerWidth: width, innerHeight: height } = window;
    return [width, height];
}

export function useWindowDimensions() {
    const [WindowDimensions, setWindowDimensions] = React.useState(
        getWindowDimensions()
    );

    React.useEffect(() => {
        function handleResize() {
            setWindowDimensions(getWindowDimensions());             
        }

        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, []);

    return WindowDimensions;
}
