import pytest
import sys
from io import StringIO
from streamlit_crewai_process_output import CrewAIProcessOutput
from streamlit_crewai_process_output.process_output import Line

def test_line_creation():
    """Test Line dataclass creation"""
    line = Line(text="test text", type="normal")
    assert line.text == "test text"
    assert line.type == "normal"

def test_process_output_initialization():
    """Test CrewAIProcessOutput initialization"""
    output = CrewAIProcessOutput()
    assert output.lines == []

def test_ansi_code_cleaning():
    """Test ANSI escape code cleaning"""
    output = CrewAIProcessOutput()
    text_with_ansi = "\033[1;32mHello\033[0m"
    cleaned = output._clean_ansi(text_with_ansi)
    assert cleaned == "Hello"
    
    # Test with multiple ANSI codes
    complex_ansi = "\033[1m\033[31mError\033[0m: \033[36mMessage\033[0m"
    cleaned = output._clean_ansi(complex_ansi)
    assert cleaned == "Error: Message"

def test_line_type_detection():
    """Test automatic line type detection"""
    output = CrewAIProcessOutput()
    
    # Test agent detection
    assert output._detect_line_type("Agent: Hello") == "agent"
    assert output._detect_line_type("👤 Agent: Hello") == "agent"
    
    # Test task detection
    assert output._detect_line_type("Task: Do something") == "task"
    assert output._detect_line_type("✅ Task: Do something") == "task"
    
    # Test thought detection
    assert output._detect_line_type("Thought: Thinking...") == "thought"
    assert output._detect_line_type("💭 Thought: Thinking...") == "thought"
    
    # Test tool detection
    assert output._detect_line_type("Tool Input: query") == "tool"
    assert output._detect_line_type("Tool Output: result") == "tool"
    assert output._detect_line_type("🔧 Tool Input: result") == "tool"
    
    # Test search detection
    assert output._detect_line_type("Search results for...") == "search"
    assert output._detect_line_type("🔍 Search results for...") == "search"
    
    # Test normal text
    assert output._detect_line_type("Regular text") == "normal"
    assert output._detect_line_type("") == "normal"

def test_add_line():
    """Test adding lines with and without type detection"""
    output = CrewAIProcessOutput()
    
    # Add line with explicit type
    output.add_line("Hello", line_type="normal")
    assert len(output.lines) == 1
    assert output.lines[0].text == "Hello"
    assert output.lines[0].type == "normal"
    
    # Add line with automatic type detection
    output.add_line("Agent: Hello")
    assert len(output.lines) == 2
    assert output.lines[1].text == "Agent: Hello"
    assert output.lines[1].type == "agent"
    
    # Test adding empty line
    output.add_line("")
    assert len(output.lines) == 3
    assert output.lines[2].text == ""
    assert output.lines[2].type == "normal"

def test_clear():
    """Test clearing all lines"""
    output = CrewAIProcessOutput()
    output.add_line("test")
    assert len(output.lines) == 1
    
    output.clear()
    assert len(output.lines) == 0

def test_capture_context_manager():
    """Test the capture context manager"""
    output = CrewAIProcessOutput()
    
    class MockContainer:
        def empty(self):
            class MockPlaceholder:
                def markdown(self, text, unsafe_allow_html=False):
                    pass
            return MockPlaceholder()
    
    # Save original stdout
    original_stdout = sys.stdout
    
    with CrewAIProcessOutput.capture(MockContainer()) as captured:
        assert isinstance(captured, CrewAIProcessOutput)
        # Write something to stdout
        print("Test output")
        
    # Check that stdout is restored
    assert sys.stdout == original_stdout

def test_stdout_capture():
    """Test that stdout is properly captured and processed"""
    output = CrewAIProcessOutput()
    mock_stdout = StringIO()
    
    # Replace stdout temporarily
    original_stdout = sys.stdout
    sys.stdout = mock_stdout
    
    try:
        print("Test output")
        # Simulate what the context manager would do
        content = mock_stdout.getvalue()
        output.add_line(content.strip())
        
        assert len(output.lines) == 1
        assert output.lines[0].text == "Test output"
        assert output.lines[0].type == "normal"
    finally:
        # Restore stdout
        sys.stdout = original_stdout

def test_emoji_handling():
    """Test that emojis are properly handled"""
    output = CrewAIProcessOutput()
    
    # Test emoji at start
    output.add_line("🤖 Robot message")
    assert output.lines[-1].text == "🤖 Robot message"
    
    # Test emoji in middle
    output.add_line("Message with 🎉 emoji")
    assert output.lines[-1].text == "Message with 🎉 emoji"
    
    # Test multiple emojis
    output.add_line("🌟 Star 💫 Sparkle")
    assert output.lines[-1].text == "🌟 Star 💫 Sparkle"
