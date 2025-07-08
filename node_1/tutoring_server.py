import grpc
from concurrent import futures
import tutoring_pb2
import tutoring_pb2_grpc
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import logging

logging.basicConfig(level=logging.INFO)

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def GetLLMAnswer(self, request, context):
    query = request.query
    # Tokenize the input with padding and truncation
    inputs = tokenizer(query, return_tensors="pt", padding=True, truncation=True)

    # Check if the attention mask is generated
    if "attention_mask" not in inputs:
        # If not, you can manually create an attention mask
        inputs["attention_mask"] = (inputs["input_ids"] != tokenizer.pad_token_id).long()

    # Generate the output with the necessary parameters
    outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],  # Ensure you provide the attention mask
        pad_token_id=tokenizer.eos_token_id,  # Set pad token ID
        do_sample=True,  # Enable sampling
        temperature=0.6,
        top_p=0.85,
        max_length=60  # You can adjust this as needed
    )

    # Decode the output to get the answer
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return tutoring_pb2.GetLLMAnswerResponse(success=True, answer=answer)
def generate_gpt2_response(query):
    inputs = tokenizer.encode(query, return_tensors="pt")
    outputs = model.generate(inputs, max_length=60, temperature=0.6, top_k=50, top_p=0.85, no_repeat_ngram_size=3)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

class TutoringServer(tutoring_pb2_grpc.TutoringServicer):
    def GetLLMAnswer(self, request, context):
        logging.info(f"Received tutoring request: {request.query}")
        answer = generate_gpt2_response(request.query)
        return tutoring_pb2.GetLLMAnswerResponse(success=True, answer=answer)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tutoring_pb2_grpc.add_TutoringServicer_to_server(TutoringServer(), server)
    server.add_insecure_port('[::]:50052')
    logging.info("Tutoring server running on port 50052")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
