
import glob
import replicate 
MyReplicate = replicate.client.Client(api_token="r8_OpRPzGcQ1PyIrGdHFrLRIHtefVSt3ZG2kgqmC")

images = glob.glob("img/*.jpg")

model = MyReplicate.models.create( 
    owner="gufu1995",
    name="flux-schnell",
    visibility="private",
    hardware="gpu-t4",
    description="A fine tuned Flux.1-schnell model for generating images of myself."
)

print(f"Model created: {model.name}")
