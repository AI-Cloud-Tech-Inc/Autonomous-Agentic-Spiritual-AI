interface ReflectionPromptProps {
  prompt: string;
}

function ReflectionPrompt({ prompt }: ReflectionPromptProps) {
  return (
    <div
      style={{
        padding: 24,
        backgroundColor: "var(--color-surface)",
        border: "1px solid var(--color-border)",
        borderRadius: 12,
        fontFamily: "var(--font-display)",
        fontStyle: "italic",
        textAlign: "center",
        color: "var(--color-text-muted)",
        lineHeight: 1.8,
      }}
    >
      {prompt}
    </div>
  );
}

export default ReflectionPrompt;
