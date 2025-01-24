from pathlib import Path
from phi.assistant import Assistant
#from phi.llm.ollama import Ollama

# assistant = Assistant(llm=Ollama(model="llama3.2-vision"))

# image_path = Path(__file__).parent / "assets/Gi CaMKII CNO 7-18 N 9-2_frame11316.png"
# assistant.print_response(
#     "Whats in the image?",
#     images=[image_path.read_bytes()],
#     markdown=True,
# )

from phi.agent import Agent
from phi.model.ollama import Ollama
from annolid.agents.clip_embedder import CLIPEmbedder
from phi.vectordb.lancedb import LanceDb, SearchType
from annolid.agents.image_knowledge import ImageKnowledgeBase

# Create a knowledge base from a PDF
knowledge_base = ImageKnowledgeBase(
    path="/Users/chenyang/Downloads/annolid_test_videos_frames",
    # Use LanceDB as the vector database
    vector_db=LanceDb(
        table_name="frames",
        uri="lancedb",
        search_type=SearchType.vector,
        embedder=CLIPEmbedder(),
    ),
)
# Comment out after first run as the knowledge base is loaded
knowledge_base.load()

agent = Agent(
    model=Ollama(id="llama3.2"),
    # Add the knowledge base to the agent
    knowledge=knowledge_base,
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)
agent.print_response("nose to nose sniffing", stream=True)
