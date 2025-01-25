from smolagents import CodeAgent, LiteLLMModel, Tool
import os
import glob
from typing import List, Dict, Any, Optional
import fnmatch

class FileManager:
    def __init__(self):
        self.base_dir = os.path.abspath(os.getcwd())  # Initialize base_dir first
        self.ignored_patterns = self._read_gitignore()  # Then read gitignore
    
    def _read_gitignore(self) -> List[str]:
        """Read .gitignore file and return list of patterns to ignore"""
        patterns = []
        gitignore_path = os.path.join(self.base_dir, '.gitignore')
        if os.path.exists(gitignore_path):
            with open(gitignore_path, 'r') as f:
                patterns = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        return patterns
    
    def _should_ignore(self, path: str) -> bool:
        """Check if a path should be ignored based on .gitignore patterns"""
        # Convert absolute path to relative path for pattern matching
        rel_path = os.path.relpath(path, self.base_dir)
        for pattern in self.ignored_patterns:
            if fnmatch.fnmatch(rel_path, pattern):
                return True
        return False
    
    def find_relevant_files(self, query: str, file_types: Optional[List[str]] = None) -> List[str]:
        """Find files relevant to the search query, respecting .gitignore"""
        if file_types is None:
            file_types = ['*.py', '*.txt', '*.md', '*.json']
            
        relevant_files = []
        for file_type in file_types:
            # Use os.path.join for proper path construction
            search_pattern = os.path.join(self.base_dir, '**', file_type)
            
            # Convert to proper path format for the current OS
            search_pattern = os.path.normpath(search_pattern)
            
            for file_path in glob.glob(search_pattern, recursive=True):
                abs_path = os.path.abspath(file_path)
                if not self._should_ignore(abs_path):
                    try:
                        with open(abs_path, 'r', encoding='utf-8') as f:
                            content = f.read().lower()
                            if query.lower() in content:
                                relevant_files.append(abs_path)
                    except Exception as e:
                        print(f"Error reading {abs_path}: {e}")
        
        return relevant_files


class AbdellahTool(Tool):
    name = "abdellah_tool"
    description = "This tool performs Abdellah task by appending 'Abdellah' to a number"
    inputs = {"number": {"type": "integer", "description": "The number to process"}}
    output_type = "string"

    def forward(self, number: int) -> str:
        return f"{number}Abdellah"

class TextAnalysisTool(Tool):
    name = "text_analysis"
    description = "Analyzes text content for various metrics"
    inputs = {"text": {"type": "string", "description": "Text to analyze"}}
    output_type = "object"

    def forward(self, text: str) -> Dict[str, Any]:
        return {
            "word_count": len(text.split()),
            "char_count": len(text),
            "line_count": len(text.splitlines()),
            "unique_words": len(set(text.lower().split()))
        }

class FileReaderTool(Tool):
    name = "file_reader"
    description = "Reads and returns the content of a file"
    inputs = {"file_path": {"type": "string", "description": "Path to the file to read"}}
    output_type = "string"

    def forward(self, file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"

def create_agent(model_id: str = "openai/gpt-4o") -> CodeAgent:
    """Create a CodeAgent with all available tools"""
    model = LiteLLMModel(model_id=model_id)
    
    tools = [
        # AbdellahTool(),
        # FileSearchTool(),
        # TextAnalysisTool(),
        # FileReaderTool()
    ]
    
    additional_imports = [
        'requests',
        'bs4',
        'pandas',
        'numpy',
        'json',
        'yaml',
        'os',
        'sys',
        'glob',
        'datetime'
    ]
    
    return CodeAgent(
        tools=tools,
        model=model,
        additional_authorized_imports=additional_imports
    )

# Example usage
if __name__ == "__main__":
    agent = create_agent()
    
    # # Example 1: Using AbdellahTool
    # result1 = agent.run("Do an abdellah task on number 5?")
    # print("Result 1:", result1)
    
    # Example 2: Search for files containing "python"
    result2 = agent.run('Find python files in the current directory and print the first 10 lines of their content')
    print("Result 2:", result2)
    