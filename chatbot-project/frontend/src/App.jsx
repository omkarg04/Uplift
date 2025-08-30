export default function App() {
  const openChatbot = () => {
    window.open(
      "https://partyrock.aws/u/iomkar04/u7zZylGVQ/Uplift%3A-Your-Emotional-Companion",  // 🔗 replace with your chatbot link
      "_blank",
      "width=1000,height=700"
    );
  };

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",   // full screen height
        backgroundColor: "#f9fafb" // light background
      }}
    >
      <button
        onClick={openChatbot}
        style={{
          padding: "14px 28px",
          backgroundColor: "#2563eb", // nice blue
          color: "white",
          border: "none",
          borderRadius: "10px",
          fontSize: "20px",
          fontWeight: "600",
          cursor: "pointer",
          boxShadow: "0 4px 6px rgba(0,0,0,0.1)"
        }}
      >
        Chat with AI Companion 
      </button>
    </div>
  );
}
