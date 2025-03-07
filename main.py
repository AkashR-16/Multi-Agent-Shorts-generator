import os
import asyncio
import requests
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console

from tools import generate_video, generate_images, generate_voiceovers

from pydantic import BaseModel

from dotenv import load_dotenv
load_dotenv()


# Define output structure for the script
class ScriptOutput(BaseModel):
    topic: str
    takeaway: str
    captions: list[str]


async def main():
    ollama_client=OllamaChatCompletionClient(
        model="llama3.1:latest",  # Use any local ollama model
        response_format=ScriptOutput
    )

    # Create agents
    script_writer = AssistantAgent(
        name="script_writer",
        model_client=ollama_client,  # Swap with ollama_client if needed
        system_message='''
            You are a creative assistant tasked with writing a script for a short video. 
            The script should consist of captions designed to be displayed on-screen, with the following guidelines:
                1.	Each caption must be short and impactful (no more than 8 words) to avoid overwhelming the viewer.
                2.	The script should have exactly 5 captions, each representing a key moment in the story.
                3.	The flow of captions must feel natural, like a compelling voiceover guiding the viewer through the narrative.
                4.	Always start with a question or a statement that keeps the viewer wanting to know more.
                5.  You must also include the topic and takeaway in your response.
                6.  The caption values must ONLY include the captions, no additional meta data or information.

        '''
    )

    voice_actor = AssistantAgent(
        name="voice_actor",
        model_client=ollama_client,
        tools=[generate_voiceovers],
        system_message='''
            You are a helpful agent tasked with generating and saving voiceovers.
            Only respond with 'TERMINATE' once files are successfully saved locally.
        '''
    )

    graphic_designer = AssistantAgent(
        name="graphic_designer",
        model_client=ollama_client,
        tools=[generate_images],
        system_message='''
            You are a helpful agent tasked with generating and saving images for a short video.
            You are given a list of captions.
            You will convert each caption into an optimized prompt for the image generation tool.
            Your prompts must be concise and descriptive and maintain the same style and tone as the captions while ensuring continuity between the images.
            Your prompts must mention that the output images MUST be in: "Abstract Art Style / Ultra High Quality." (Include with each prompt)
            You will then use the prompts list to generate images for each provided caption.
            Only respond with 'TERMINATE' once the files are successfully saved locally.
        '''
    )

    director = AssistantAgent(
        name="director",
        model_client=ollama_client,
        tools=[generate_video],
        system_message='''
            You are a helpful agent tasked with generating a short video.
            You are given a list of captions which you will use to create the short video.
            Remove any characters that are not alphanumeric or spaces from the captions.
            You will then use the captions list to generate a video.
            Only respond with 'TERMINATE' once the video is successfully generated and saved locally.
        '''
    )

    # Set up termination condition
    termination = TextMentionTermination("TERMINATE")
    
    # Create sequential execution order
    # Use different agent groups with different max_rounds to ensure each agent completes its task
    agent_team = RoundRobinGroupChat(
        [script_writer, voice_actor, graphic_designer, director],
        termination_condition=termination,
        # Each agent gets one full turn
        max_turns=4
    )

    # Interactive console loop
    while True:
        user_input = input("Enter a message (type 'exit' to leave): ")
        if user_input.strip().lower() == "exit":
            break
        
        # Run the team with the user input and display results
        stream = agent_team.run_stream(task=user_input)
        await Console(stream)

# Run the main async function
if __name__ == "__main__":
    asyncio.run(main())