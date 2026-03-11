class ConversationalOrchestrator:
    def __init__(self,intent_detector, state_machine, context_manager, tool_router):
        self.intent_detector = intent_detector;
        self.state_machine = state_machine
        self.context_manager = context_manager
        self.tool_router = tool_router


    async def handle_message(self, user_id, message):
        context = await self.context_manager.get_context(user_id)
        intent = self.intent_detector.detect(message)
        new_state = self.state_machine.transition(context, intent)
        tool = self.tool_router.route(intent)
        result = await tool.run(message, context)
        
        await self.context_manager.update(user_id, new_state)
        return result
    

    
        