# def pretty_print_thread_messages(messages):
#     from colorama import init, Fore, Style
#     import textwrap

#     # Initialize colorama
#     init()

#     print(f"{Fore.GREEN}{'=' * 60}{Style.RESET_ALL}")
#     print(f"{Fore.GREEN}Thread Messages{Style.RESET_ALL}".center(60))
#     print(f"{Fore.GREEN}{'=' * 60}{Style.RESET_ALL}")

#     for m in reversed(messages.data):
#         role_color = Fore.BLUE if m.role == "user" else Fore.GREEN
#         role_icon = "👤" if m.role == "user" else "🤖"
        
#         print(f"\n{role_color}{role_icon} {m.role.upper()}{Style.RESET_ALL}")
#         print(f"{role_color}{'-' * 60}{Style.RESET_ALL}")
        
#         message_text = m.content[0].text.value
#         citations = []
        
#         # Handle annotations if they exist
#         if hasattr(m.content[0].text, 'annotations'):
#             # Process annotations to replace citation markers with footnote numbers
#             annotations = m.content[0].text.annotations
#             if annotations:
#                 # Sort annotations by start_index in reverse order to avoid index issues when replacing
#                 sorted_annotations = sorted(annotations, key=lambda a: a.start_index, reverse=True)
                
#                 for i, annotation in enumerate(sorted_annotations, 1):
#                     if hasattr(annotation, 'text'):
#                         # Get start and end indices
#                         start_idx = annotation.start_index
#                         end_idx = annotation.end_index
                        
#                         # Replace citation text with footnote number
#                         if start_idx is not None and end_idx is not None:
#                             message_text = message_text[:start_idx] + f"[{i}]" + message_text[end_idx:]
                        
#                     # Add citation to list
#                     if hasattr(annotation, 'url_citation'):
#                         citations.append((i, f"{annotation.url_citation.title}: {annotation.url_citation.url}"))
        
#         # Print the processed message with word wrapping
#         wrapped_text = textwrap.fill(message_text, width=80)
#         print(wrapped_text)
        
#         # Print citations if they exist
#         if citations:
#             print(f"\n{Fore.YELLOW}Citations:{Style.RESET_ALL}")
#             for i, citation in citations:
#                 print(f"{i}. {citation}")
#         print()

def pretty_print_thread_messages(messages):
    from colorama import init, Fore, Style
    import textwrap
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.panel import Panel

    # Initialize colorama and rich console
    init()
    console = Console(highlight=False)

    for m in reversed(messages.data):
        role_color = Fore.BLUE if m.role == "user" else Fore.GREEN
        role_icon = "👤" if m.role == "user" else "🤖"
        
        print(f"\n{role_color}{role_icon} {m.role.upper()}{Style.RESET_ALL}")
        print(f"{role_color}{'-' * 60}{Style.RESET_ALL}")
        
        message_text = m.content[0].text.value
        citations = []
        
        # Handle annotations if they exist
        if hasattr(m.content[0].text, 'annotations'):
            annotations = m.content[0].text.annotations
            if annotations:
                # Sort annotations by start_index in reverse order to avoid index issues when replacing
                sorted_annotations = sorted(annotations, key=lambda a: a.start_index, reverse=True)
                
                for i, annotation in enumerate(sorted_annotations, 1):
                    if hasattr(annotation, 'text'):
                        # Get start and end indices
                        start_idx = annotation.start_index
                        end_idx = annotation.end_index
                        
                        # Replace citation text with footnote number
                        if start_idx is not None and end_idx is not None:
                            message_text = message_text[:start_idx] + f"[{i}]" + message_text[end_idx:]
                        
                    # Add citation to list
                    if hasattr(annotation, 'url_citation'):
                        citations.append((i, f"{annotation.url_citation.title}: {annotation.url_citation.url}"))
        
        # Render the markdown content
        md = Markdown(message_text)
        console.print(md)
        
        # Print citations if they exist
        if citations:
            print(f"\n{Fore.YELLOW}Citations:{Style.RESET_ALL}")
            for i, citation in citations:
                print(f"{i}. {citation}")