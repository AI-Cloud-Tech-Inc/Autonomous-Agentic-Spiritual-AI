import { ReactNode } from "react";

interface LayoutProps {
  children: ReactNode;
}

function Layout({ children }: LayoutProps) {
  return (
    <div style={{ minHeight: "100vh", display: "flex", flexDirection: "column" }}>
      <header
        style={{
          padding: "12px 24px",
          borderBottom: "1px solid var(--color-border)",
          fontFamily: "var(--font-display)",
          fontSize: "1.1rem",
        }}
      >
        Spiritual AI
      </header>
      <main style={{ flex: 1 }}>{children}</main>
    </div>
  );
}

export default Layout;
