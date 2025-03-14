import os
import re
import sys
import glob

def check_anchors(content_dir):    
    """    Checks for broken anchor links in Hugo content files.    """    
    markdown_files = glob.glob(os.path.join(content_dir, "**/*.md"), recursive=True)   

    all_anchors = {}    
    for file_path in markdown_files:      
        with open(file_path, 'r', encoding='utf-8') as file:        
            content = file.read()        

            # Extract all anchors (both manual and auto-generated)        
            anchors = re.findall(r'{#([\w-]+)}|id="([\w-]+)"', content)                
            # Store anchors with file paths        
            for anchor_tuple in anchors:            
                anchor = next((a for a in anchor_tuple if a), None)            
                if anchor:                
                    if anchor not in all_anchors:                  
                        all_anchors[anchor] = []                
                        all_anchors[anchor].append(file_path)    
    errors = False    
    for file_path in markdown_files:        
        with open(file_path, 'r', encoding='utf-8') as file:            
            content = file.read()            
            # Find all links with anchors            
            links_with_anchors = re.findall(r'\[.*?\]\((.*?)(#[\w-]+)\)', content)            
            for link, anchor in links_with_anchors:                
                if anchor[1:] not in all_anchors:                    
                    print(f"Error: Broken anchor link in {file_path}: {link}{anchor}")                    
                    errors = True    
    if not errors:        
        print("No broken anchor links found.")    
        return not errors
    
if __name__ == "__main__":    
    if len(sys.argv) != 2:        
        print("Usage: python check_anchors.py <content_directory>")        
        sys.exit(1)    
    content_directory = sys.argv[1]    
    if not os.path.isdir(content_directory):        
        print(f"Error: Directory not found: {content_directory}")        
        sys.exit(1)    
    if not check_anchors(content_directory):      
        sys.exit(1)