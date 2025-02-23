from abc import ABC, abstractmethod
import re

class TranscriptionParser(ABC):
    """Abstract base class for transcription parsers"""
    
    @abstractmethod
    def parse(self, content: str) -> str:
        """Parse the transcription content"""
        pass
    
    @abstractmethod
    def can_parse(self, content: str) -> bool:
        """Determine if this parser can handle the content"""
        pass

class TimestampedTranscriptionParser(TranscriptionParser):
    """Parser for transcriptions with timestamps [HH:MM]"""
    
    def can_parse(self, content: str) -> bool:
        return bool(re.search(r'\[\d{2}:\d{2}\]', content))
    
    def parse(self, content: str) -> str:
        lines = content.split('\n')
        parsed_lines = []
        current_timestamp = None
        
        for line in lines:
            # Detect timestamp
            timestamp_match = re.match(r'\[(\d{2}:\d{2})\]', line)
            if timestamp_match:
                current_timestamp = timestamp_match.group(0)
                line = line[7:].strip()  # Remove timestamp from text
            
            if line:
                if current_timestamp and not parsed_lines:
                    parsed_lines.append(current_timestamp)
                parsed_lines.append(line)
                
        return '\n'.join(parsed_lines)

class PlainTranscriptionParser(TranscriptionParser):
    """Parser for transcriptions without special formatting"""
    
    def can_parse(self, content: str) -> bool:
        return True  # This parser handles any plain text
    
    def parse(self, content: str) -> str:
        # Normalize text
        lines = content.split('\n')
        parsed_lines = [line.strip() for line in lines if line.strip()]
        return '\n'.join(parsed_lines) 