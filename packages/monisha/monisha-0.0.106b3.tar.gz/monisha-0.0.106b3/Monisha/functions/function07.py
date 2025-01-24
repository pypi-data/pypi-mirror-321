import asyncio
from .collections import SMessage
#======================================================================================

async def commandR(command, **kwargs):
    try:
        mainos = await asyncio.create_subprocess_exec(*command,
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, **kwargs) 
        moonus = await mainos.communicate()
        moon01 = moonus[0]
        moon02 = moonus[1]
        result = moon01.strip()
        errors = moon02.strip()
        codeos = mainos.returncode
        return SMessage(results=result, taskcode=codeos, errors=errors)
    except Exception as errors:
        return SMessage(errors=errors)

#======================================================================================
