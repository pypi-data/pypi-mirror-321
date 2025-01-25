import vertexai
import vertexai.generative_models as gm
import google.generativeai as genai
import PIL.Image
import os


def make_llm_call_vertex(image_path: str, system_message: str, model: str, project_id: str, location: str, response_schema: dict = None, max_tokens: int = 4000) -> str:
    """
    This function calls the Vertex AI Gemini API (not to be confused with the Gemini API) with an image and a system message and returns the response text.
    """
    vertexai.init(project=project_id, location=location)
    model = gm.GenerativeModel(model)
    
    if response_schema is not None:
        generation_config = gm.GenerationConfig(temperature=0.0, max_output_tokens=max_tokens, response_mime_type="application/json", response_schema=response_schema)
    else:
        generation_config = gm.GenerationConfig(temperature=0.0, max_output_tokens=max_tokens)
    
    response = model.generate_content(
        [
            gm.Part.from_image(gm.Image.load_from_file(image_path)),
            system_message,
        ],
        generation_config=generation_config,
    )
    return response.text


def compress_image(image: PIL.Image.Image, max_size: tuple[int, int] = (3000, 3000)) -> PIL.Image.Image:
    """
    Compress image if it exceeds maximum dimensions while maintaining aspect ratio.
    """
    if image.size[0] > max_size[0] or image.size[1] > max_size[1]:
        image.thumbnail(max_size, PIL.Image.Resampling.LANCZOS)
    return image


def make_llm_call_gemini(image_path: str, system_message: str, model: str = "gemini-1.5-pro-002", response_schema: dict = None, max_tokens: int = 4000) -> str:
    
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    generation_config = {
        "temperature": 0,
        "response_mime_type": "application/json",
        "max_output_tokens": max_tokens
    }
    if response_schema is not None:
        generation_config["response_schema"] = response_schema

    model = genai.GenerativeModel(model)
    try:
        image = PIL.Image.open(image_path)
        # Compress image if needed
        image = compress_image(image)
        response = model.generate_content(
            [
                image,
                system_message
            ],
            generation_config=generation_config
        )
        return response.text
    finally:
        # Ensure image is closed even if an error occurs
        if 'image' in locals():
            image.close()