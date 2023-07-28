import asab.web
import asab.web.rest
import bspump
from pipeline import TCPPipeline


class BlankAppApplication(bspump.BSPumpApplication):

	def __init__(self):
		super().__init__()
		# Initialize BSPump Service
		self.BSPumpService = self.get_service("bspump.PumpService")

		# Load the webservice module
		from asab.web import Module
		self.add_module(Module)

		# Locate webservice
		self.WebService = self.get_service("asab.WebService")
		self.WebContainer = asab.web.WebContainer(self.WebService, "web")
		self.WebContainer.WebApp.middlewares.append(asab.web.rest.JsonExceptionMiddleware)

		# Load blank module
		from .module import BlankModule
		self.add_module(BlankModule)

		# Register pipeline
		self.BSPumpService.add_pipeline(TCPPipeline(self, "TCPPipeline"))
