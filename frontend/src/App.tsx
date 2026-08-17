import { useEffect, useState } from "react"

function App() {
  const [status, setStatus] = useState("Checking...")

  useEffect(() => {
    fetch("http://127.0.0.1:8000/health")
      .then(res => res.json())
      .then(data => setStatus(data.status === "ok" ? "Connected" : "Error"))
      .catch(() => setStatus("Disconnected"))
  }, [])

  return (
    <div>
      <h1>AgentForge</h1>
      <p>Multi-Agent Orchestration Platform</p>
      <p>Backend: {status}</p>
    </div>
  )
}

export default App