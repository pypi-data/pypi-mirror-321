import re
from dataclasses import dataclass
from typing import List, Optional
import streamlit as st
import sys
from contextlib import contextmanager

@dataclass
class Line:
    """A line of process output with its type."""
    text: str
    type: str

class CrewAIProcessOutput:
    """A component for displaying CrewAI agent process outputs in Streamlit applications."""
    
    def __init__(self):
        """Initialize the process output component."""
        self.lines: List[Line] = []

    def _clean_ansi(self, text: str) -> str:
        """Remove ANSI escape codes from text."""
        return re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', text)

    def _detect_line_type(self, text: str) -> str:
        """Detect the type of line based on content."""
        text = self._clean_ansi(text)
        if "Agent:" in text:
            return "agent"
        elif "Task:" in text:
            return "task"
        elif "Thought:" in text:
            return "thought"
        elif "Tool Input:" in text or "Tool Output:" in text:
            return "tool"
        elif "Search results" in text:
            return "search"
        return "normal"

    def add_line(self, text: str, line_type: Optional[str] = None):
        """
        Add a line to the process output.
        Args:
            text (str): The text content of the line
            line_type (str, optional): Type of line. If None, type will be auto-detected.
        """
        cleaned_text = self._clean_ansi(text)
        detected_type = line_type or self._detect_line_type(text)
        self.lines.append(Line(text=cleaned_text, type=detected_type))

    def clear(self):
        """Clear all lines from the process output."""
        self.lines = []

    def render(self, container):
        """
        Render the process output in a Streamlit container.
        
        Args:
            container: A Streamlit container to render the process output in
        """
        if not self.lines:
            return

        # Add regex pattern for extracting URLs
        url_pattern = re.compile(r'href="([^"]+)"')
        
        def clean_html(text):
            """Remove HTML tags and extract clean text"""
            # Remove any existing HTML tags
            text = re.sub(r'<[^>]+>', '', text)
            # Unescape any HTML entities
            text = text.replace('&lt;', '<').replace('&gt;', '>')
            return text.strip()
        
        def extract_url(text):
            """Extract URL from text that might contain HTML"""
            # First try to find URL in href
            url_match = url_pattern.search(text)
            if url_match:
                return url_match.group(1)
            # If no href, try to find a plain URL
            url_match = re.search(r'https?://[^\s<>"]+', text)
            if url_match:
                return url_match.group(0)
            return ''

        # Apply custom styling
        container.markdown("""
        <style>
        .friendly-output {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 20px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 15px;
            line-height: 1.6;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin: 10px 0;
        }
        .agent-message {
            font-weight: 500;
            margin-bottom: 8px;
        }
        .task-message {
            font-weight: 500;
            margin: 12px 0;
        }
        .thought-message {
            font-style: italic;
            margin: 8px 0;
            padding-left: 12px;
            border-left: 3px solid #e0e0e0;
        }
        .tool-message {
            margin: 8px 0;
        }
        .search-result {
            background-color: #f7fafc;
            border-radius: 8px;
            padding: 12px;
            margin: 8px 0;
        }
        .search-result a {
            text-decoration: none;
            border-bottom: 1px solid;
        }
        .search-result a:hover {
            opacity: 0.8;
        }
        </style>
        """, unsafe_allow_html=True)

        # Format the output with custom styling
        output_lines = []
        current_search_results = []
        
        for line in self.lines:
            text = line.text.rstrip()
            
            # Convert URLs to clickable links
            if not line.type == 'search':  # Skip URL conversion for search results
                text = re.sub(
                    r'(https?://[^\s]+)',
                    r'<a href="\1" target="_blank">\1</a>',
                    text
                )

            # Clean up the prefixes to make them more user-friendly and bold
            text = text.replace('# Agent:', '<strong>🤖 Agent:</strong>')
            text = text.replace('## Task:', '<strong>🎯 Task:</strong>')
            text = text.replace('## Thought:', '<strong>💭 Thought:</strong>')
            text = text.replace('## Using tool:', '<strong>🔧 Using tool:</strong>')
            text = text.replace('## Tool Input:', '<strong>📝 Tool Input:</strong>')
            text = text.replace('## Tool Output:', '<strong>📄 Tool Output:</strong>')
            
            # Add appropriate styling based on line type
            if line.type == 'agent':
                # Add spacing before agent messages
                output_lines.append(f'<div style="margin-top: 20px;"></div>')
                output_lines.append(f'<div class="agent-message">{text}</div>')
            elif line.type == 'task':
                # Add spacing before tasks
                output_lines.append(f'<div style="margin-top: 15px;"></div>')
                output_lines.append(f'<div class="task-message">{text}</div>')
            elif line.type == 'thought':
                # Add spacing before thoughts
                output_lines.append(f'<div style="margin-top: 15px;"></div>')
                output_lines.append(f'<div class="thought-message">{text}</div>')
            elif line.type == 'tool':
                if 'Tool Input:' in text:
                    # Add spacing before tool input
                    output_lines.append(f'<div style="margin-top: 15px;"></div>')
                    output_lines.append(f'<div class="tool-message" style="margin-left: 20px;">{text}</div>')
                elif 'Tool Output:' in text:
                    # Add spacing before tool output
                    output_lines.append(f'<div style="margin-top: 15px;"></div>')
                    output_lines.append(f'<div class="tool-message" style="margin-left: 20px;">{text}</div>')
                else:
                    output_lines.append(f'<div class="tool-message">{text}</div>')
            elif line.type == 'search':
                if text.startswith('Search results:'):
                    # Add spacing before search results
                    output_lines.append(f'<div style="margin-top: 15px;"></div>')
                    output_lines.append(f'<div style="margin-left: 20px;">{text}</div>')
                elif text.startswith(('Title:', 'Link:', 'Snippet:')):
                    # Indent and format search result components
                    text = text.replace('Title:', '<strong>Title:</strong>')
                    text = text.replace('Link:', '<strong>Link:</strong>')
                    text = text.replace('Snippet:', '<strong>Snippet:</strong>')
                    output_lines.append(f'<div style="margin-left: 40px;">{text}</div>')
                    # Add small spacing after each complete search result (after Snippet)
                    if text.startswith('Snippet:'):
                        output_lines.append(f'<div style="margin-top: 10px;"></div>')
                else:
                    output_lines.append(f'<div style="margin-left: 20px;">{text}</div>')
            elif not any(skip in text.lower() for skip in ['"search_query"', '---']):
                output_lines.append(f'<div>{text}</div>')

        # Join lines and render
        html_output = f'<div class="friendly-output">{"".join(output_lines)}</div>'
        container.markdown(html_output, unsafe_allow_html=True)

    @classmethod
    @contextmanager
    def capture(cls, container: st.container):
        """
        Context manager to capture CrewAI output in a Streamlit container.
        
        Example:
            ```python
            with CrewAIProcessOutput.capture(st.container()):
                # Run your CrewAI code here
                crew.kickoff()
            ```
        """
        output = cls()
        placeholder = container.empty()
        
        class StdoutRedirector:
            def write(self, text):
                output.add_line(text)
                output.render(placeholder)
            def flush(self):
                pass
        
        old_stdout = sys.stdout
        sys.stdout = StdoutRedirector()
        try:
            yield output
        finally:
            sys.stdout = old_stdout
