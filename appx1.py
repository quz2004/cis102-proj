import streamlit as st

def main():
    # Add custom CSS to create a highlight effect
    st.markdown(
        """
        <style>
        ::selection {
            background-color: yellow;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Load JavaScript code to handle the popup textbox
    st.markdown(
        """
        <script>
        document.addEventListener('mouseup', function() {
            var selectedText = window.getSelection().toString().trim();
            if (selectedText !== '') {
                var userInput = prompt('You selected: ' + selectedText);
                if (userInput !== null) {
                    alert('You entered: ' + userInput);
                }
            }
        });
        </script>
        """,
        unsafe_allow_html=True
    )

    # Display some text for highlighting
    st.markdown("""
        Select and highlight any text in this area to activate the popup textbox.
    """)

if __name__ == "__main__":
    main()

