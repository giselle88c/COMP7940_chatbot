from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters, ConversationHandler, Updater
import configparser
import os
import logging
from pymongo import MongoClient
import datetime
from ChatGPT_HKBU import HKBU_ChatGPT


config = configparser.ConfigParser()
config.read('config.ini')

DB_url=config['MONGODB']['DB_URL']

global client
client = MongoClient(DB_url)
global db 
db = client['database']
movie_list = db['movie'].distinct("name")


# Define states for the conversation
START, QACTION, ADD_COMMENT,SEARCH_MOVIE = range(4)

# Start function
def start(update: Update, context: CallbackContext) -> int:
    """Start the conversation."""
    update.message.reply_text(f'Hello, Nice to meet you. I am a movie assistant :) \nPlease enter the Movie name.')
    return START



# Function to handle movie selection and details
def user_selection(update: Update, context: CallbackContext) -> int:

    # Clean and format the movie name
    movie_name = ' '.join(update.message.text.strip().split()).title()

    context.user_data['movie_name'] = movie_name

    if movie_name in movie_list:
        global db
        document = db['movie'].find_one({'name':movie_name}, {"name": 1, "description": 1, "_id": 0})  
        movie_details = document['description']
        update.message.reply_text(f'Movie: {movie_name}\nDescription: {movie_details}\n')
        update.message.reply_text(f'/comment to give comments\n/query to view comments \n /end to end conversation')
        return QACTION
    else:
        update.message.reply_text(f'What do you want ask about {movie_name} \n /end to end conversation')
        return SEARCH_MOVIE



# Function to query movie comments
def user_search(update: Update, context: CallbackContext) -> int:
    """Query comments of a movie."""
    msg = update.message.text
    movie_name = context.user_data.get('movie_name')
    
    global chatgpt

    reply_message = chatgpt.submit(f'About this movie: {movie_name}, provide short answer following question: \n{update.message.text}')

    logging.info("Update: " + str(update))
    logging.info("context: " + str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_message)

    if(movie_name in movie_list):

        update.message.reply_text(f'Anything you want to ask about {movie_name}?')
        update.message.reply_text(f'Or enter /comment to give comments\n/query to view comments \n /end to end conversation')
        return QACTION
    else:
        update.message.reply_text(f'Anything you want to ask about {movie_name}?')
        return SEARCH_MOVIE

def ask_comment(update: Update, context: CallbackContext) -> int:

    logging.info("ask comment")
    update.message.reply_text('Please give us comments')
    return ADD_COMMENT

# Function to add comments
def add_comment(update: Update, context: CallbackContext) -> int:

    movie_name = context.user_data.get('movie_name')
    comment = update.message.text

    logging.info("movie_name: " + str(movie_name))

    if movie_name in movie_list:
        # Insert the record
        record={'name':movie_name,'comment':comment, 'datetime':datetime.datetime.now()}
        db['comment'].insert_one(record)
        update.message.reply_text(f'Thanks for your comment! :)')

        
        update.message.reply_text(f'Anything you want to ask about {movie_name}?')
        update.message.reply_text(f'Or enter /comment to give comments\n/query to view comments \n /end to end conversation')
        return QACTION
    else:
        update.message.reply_text('Sorry this movie does not exist, please try again.(1)')
        return START



def query_movie(update: Update, context: CallbackContext) -> int:
    """List comments for the queried movie."""
    movie_name = context.user_data.get('movie_name')

    #logging.info("msg: " + str(msg))
    logging.info("movie_name: " + str(movie_name))

    if movie_name in movie_list:
        comments_summary =  getMovieSummary(movie_name)
        update.message.reply_text(f'Movie: {movie_name}\nComments:\n{comments_summary}')


        update.message.reply_text(f'Anything you want to ask about {movie_name}?')
        update.message.reply_text(f'Or enter /comment to give comments about {movie_name} or \n/query to view commennts \n /end to end the conversation')
        return QACTION
    else:
        update.message.reply_text('Sorry this movie does not exist, please try again(2)')
    
    return START

def getMovieSummary(movie_name):
    
    comments_summary =''

    
    if movie_name in movie_list:
        # Retrieve and display the latest 100 comments summary

        documents = db['comment'].find({'name':movie_name},{"comment": 1,"datetime":1,"_id": 0}).sort("datetime", -1).limit(100)  # Sort by datetime descending, limit to 10
        latest_comments=list(document['comment'] for document in documents)

        if latest_comments:

            comments_summary = "\n".join(latest_comments)
            global chatgpt
            reply_message = chatgpt.submit(f'Here are the comments: {latest_comments}. Please proivde movie review summary only based on these comments without adding any extra details.')
            return reply_message
        else: return "No comments yet"
    
    return "No comments yet"
    
    

def end_conversation(update: Update, context: CallbackContext) -> int:
    
    update.message.reply_text('Goodbye ^^')
    return ConversationHandler.END  # Ends the conversation


# Main function to set up the bot and handlers
def main() -> None:
    
    updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher
    
    global chatgpt
    chatgpt = HKBU_ChatGPT(config)

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Create a conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            START: [MessageHandler(Filters.text & ~Filters.command, user_selection)],
            QACTION: [
            CommandHandler('comment', ask_comment),
            CommandHandler('query', query_movie),
            CommandHandler('end', end_conversation),
            MessageHandler(Filters.text & ~Filters.command, user_search),
            
            ],
            ADD_COMMENT: [MessageHandler(Filters.text & ~Filters.command, add_comment)],
            SEARCH_MOVIE: [
            MessageHandler(Filters.text & ~Filters.command, user_search),
            CommandHandler('end', end_conversation)
            ]
        }
        ,
        fallbacks=[],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    
    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()